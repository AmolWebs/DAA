#include<iostream>
using namespace std;

bool isSafe(int** arr, int x, int y, int n){
    //col
    for(int row = 0; row<x ; row++){
        if(arr[row][y] == 1){
            return false;
        }
    }
    //left diagonal
    int row = x;
    int col = y;
    while(row >=0 && col >= 0){
        if(arr[row][col] == 1){
            return false;
        }
        col--;
        row--;
    }

    //right diagonal
    row = x;
    col = y;
    while(row >= 0 && col < n){
        if(arr[row][col] == 1){
            return false;
        }
        col++;
        row--;
    }
    return true;
}

bool nQueen(int** arr, int x, int n){
    
}