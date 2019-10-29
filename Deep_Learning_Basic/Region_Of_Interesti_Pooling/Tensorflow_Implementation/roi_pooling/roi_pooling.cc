#include "tensorflow/core/framework/op.h"
#include "tensorflow/core/framework/op_kernel.h"
#include <cstdio>
#include <iostream>
#include <typeinfo>

/*
This source is declare Operation based on tensorflow operation kernel to be called in cuda 
This will declare Region to be applied pooling processing

*/
using namespace tensorflow;
using namespace std;
