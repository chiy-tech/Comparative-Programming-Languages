#include "covid_stat.h"
#include <math.h>
#include <stdio.h> 
#include<stdio.h> 
#include<stdlib.h> 


float calculateMEAN(float* data){
    float sum = 0.0, mean, SD = 0.0;
    int size = sizeof(data)/sizeof(data[0]);
    for (int i = 0; i < size; ++i) {
        sum += data[i];
    }
    mean = sum / size;
    return mean;
}


float calculateSD(float* data) {
    float sum = 0.0, mean, SD = 0.0;
    int size = sizeof(data)/sizeof(data[0]);
    for (int i = 0; i < size; ++i) {
        sum += data[i];
    }
    mean = sum / size;
    for (int i = 0; i < size; ++i)
        SD += pow(data[i] - mean, 2);
    return sqrt(SD / size);
}

float avGrowthEveryday(int amount, int numOfDay){
  return amount/numOfDay;
}


float rateOfMonth(float a, float b){
  return (b-a)/a;

}
float avgRateOfMonth(float a,float b,float c,float d,float e){
  float sum = 0;
  sum += a;
  sum += b;
  sum += c;
  sum += d;
  sum += e;
  return sum/5;
}

float avgRateOfMonth2(float* a){
  float sum = 0;
  for(int i = 0; i<6;i++){
    sum += a[i];
  }
  return sum/4;
}