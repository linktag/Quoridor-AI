%module cquoridor
%{
#include <Python.h>
#include <queue>
#include <set>
%}
%include "std_vector.i"
namespace std {
   %template(IntVector) vector<int>;
   %template(IntVectorVector) vector<vector<int>>;
   %template(DoubleVector) vector<double>;
   %template(DoubleVectorVector) vector<vector<double>>;
}
int BreadthFirstSearch(vector<int> positionDeDepart, int ligneAAtteindre, int barrieresHorizontales[8][8], int barrieresVerticales[8][8]);