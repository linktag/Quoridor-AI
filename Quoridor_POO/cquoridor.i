%module cquoridor
%{
#include <Python.h>
#include <queue>
#include <set>
%}
%include "std_vector.i"
namespace std {
%template(Line)  vector < int >;
    %template(Array) vector < vector < int> >;
}
int BreadthFirstSearch(vector<int> positionDeDepart, int ligneAAtteindre, std::vector< std::vector < int > > barrieresHorizontales, std::vector< std::vector < int > > barrieresVerticales);
void print_array(std::vector< std::vector < int > > myarray);