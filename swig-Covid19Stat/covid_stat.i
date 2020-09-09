%module covid_stat
%{
#include "covid_stat.h"
%}

%include "covid_stat.h"
%apply float *OUTPUT {float*};