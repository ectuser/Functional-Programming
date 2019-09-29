#define _CRT_SECURE_NO_WARNINGS	
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include "pch.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <climits>
#include <sstream>
#include <ctime>
#include <iomanip>
#include <regex>
#include <random>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <cstring>
#include <complex>
#include <cassert>
#include <iterator>
#include <functional>
#include <fstream>
using namespace std;

struct Triangle
{
	int x1, y1, x2, y2, x3, y3;
};

int get_number()
{
	int n;
	cin >> n;
	return n;
}

Triangle get_triangle()
{
	Triangle tr;
	cin >> tr.x1 >> tr.y1 >> tr.x2 >> tr.y2 >> tr.x3 >> tr.y3;
	return tr;
}

vector<Triangle> create_coord_array(int n) {
	vector<Triangle> coords(n);
	return coords;
}

vector<Triangle> triangle_loop(int index, vector<Triangle> triangles)
{
	if (index >= triangles.size())
	{
		return triangles;
	}
	triangles[index] = get_triangle();
	return triangle_loop(index + 1, triangles);

}

Triangle triangle_multiplication(int mul_number, Triangle triangle)
{
	// one particular triangle
	triangle.x1 *= mul_number;
	triangle.y1 *= mul_number;
	triangle.x2 *= mul_number;
	triangle.y2 *= mul_number;
	triangle.x3 *= mul_number;
	triangle.y3 *= mul_number;
	return triangle;
}

vector<Triangle> get_triangles_multiplication(int mul_number, vector<Triangle> triangles, int index) {
	// adding all triangles together
	if (index >= triangles.size()) {
		return triangles;
	}
	triangles[index] = triangle_multiplication(mul_number, triangles[index]);
	return get_triangles_multiplication(mul_number, triangles, index + 1);
}

Triangle count_new_vector(vector<Triangle> triangles, int index) {
	Triangle new_vector;
	new_vector.x1 = triangles[index].x2 - triangles[index].x1;
	new_vector.y1 = triangles[index].y2 - triangles[index].y1;
	// first math vector

	new_vector.x2 = triangles[index].x3 - triangles[index].x2;
	new_vector.y2 = triangles[index].y3 - triangles[index].y2;
	// second math vector

	new_vector.x3 = triangles[index].x1 - triangles[index].x3;
	new_vector.y3 = triangles[index].y1 - triangles[index].y3;
	// third math vector


	return new_vector;
}

vector<Triangle> get_vectors(vector<Triangle> triangles, int index, vector<Triangle> vectors)
{
	if (index >= triangles.size()) {
		return vectors;
	}
	vectors.push_back(count_new_vector(triangles, index)); // add math vectors (of one triangle) to vectors array
	return get_vectors(triangles, index + 1, vectors);

}

void show(vector<Triangle> result, int i)
{
	if (i < result.size())
	{
		cout << result[i].x1 << " " << result[i].y1 << " " << result[i].x2 << " " << result[i].y2 << " " << result[i].x3 << " " << result[i].y3 << endl;
		show(result, i + 1);
	}
}

vector<Triangle> create_empty_vector() {
	vector<Triangle> vectors;
	return vectors;
}

int main()
{
	show(get_vectors(get_triangles_multiplication(get_number(), triangle_loop(0, create_coord_array(get_number())), 0), 0, create_empty_vector()), 0);
}