#include "iostream"
using namespace std;

int main() {
	int x, y;
	cin >> x >> y;
	int* arr = new int[x];
	for (int i = 0; i < x; i++)
		cin >> arr[i];

	int validRoad = 0;
	for (int i = 0; i < x; i++) {
		if (arr[i] > y)
			validRoad += 2;
		else
			validRoad += 1;
	}
	cout << validRoad;
}