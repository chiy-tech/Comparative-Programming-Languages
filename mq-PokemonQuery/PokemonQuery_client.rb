# ruby PokemonQuery_client.rb
# based on https://www.rabbitmq.com/tutorials/tutorial-six-ruby.html
require 'bunny'
require 'thread'
require 'securerandom'
require 'json'
require 'csv'

class RpcClient
  attr_accessor :call_id, :response, :lock, :condition, :connection,
                :channel, :server_queue_name, :reply_queue, :exchange

  def initialize(server_queue_name)
    @connection = Bunny.new(automatically_recover: false)
    @connection.start

    @channel = connection.create_channel
    @exchange = channel.default_exchange
    @server_queue_name = server_queue_name

    setup_reply_queue
  end

  def call(arg)
    @call_id = SecureRandom.uuid
    body = JSON.generate(arg).encode('utf-8')

    exchange.publish(body,
                     routing_key: server_queue_name,
                     correlation_id: call_id,
                     reply_to: reply_queue.name)

    # wait for the signal to continue the execution
    lock.synchronize { condition.wait(lock) }

    response
  end

  def stop
    channel.close
    connection.close
  end

  private

  def setup_reply_queue
    @lock = Mutex.new
    @condition = ConditionVariable.new
    that = self
    @reply_queue = channel.queue('', exclusive: true)

    reply_queue.subscribe do |_delivery_info, properties, payload|
      if properties[:correlation_id] == that.call_id
        that.response = JSON.parse(payload.encode('utf-8'))
        # sends the signal to continue the execution of #call
        that.lock.synchronize { that.condition.signal }
      end
    end
  end
end




history = []
client = RpcClient.new('rpc_queue')
puts "================================================="
puts "Welcom to the Pokemon Query:)"
while true
  puts "------------------------------------------------"
  puts "Please enter the pokemon's key words:"
  puts "Name  (Example: Pikachu)"
  puts "Index number  (Example: 25)"
  puts "type  (Example: Grass)"
  puts "Ablity  (Example: =600, >300, <100, >=500, <=80, != 600)"
  puts "Legendary  (Example: legendary, not legendary)"
  val = gets
  puts "------------------------------------------------"
  response = client.call({:string => val})
  history.append(response)
  puts "Your result is:"
  if response == "Nothing found."
    puts response
  else 
    puts "Found! Save to history!"
  end
  #puts response
  puts "------------------------------------------------"
  puts "What do you want to do?\n1. I love Pokemon! Do it again!\n2. Cheak my history.\n3. Quit\n4. Save This Query to txt file.\nPlease enter your number:)"
  puts "---------------------"
  val = gets
  if(val == "3\n")
    break
  elsif val == "2\n"
    puts history
  elsif val == "4\n"
    open('myQuery.txt', "a") { |file| file.write(response+"\n")}
  elsif val != "1\n"
    puts "Done."
    break
  end
end
puts "Query clinet closed :)"
client.stop