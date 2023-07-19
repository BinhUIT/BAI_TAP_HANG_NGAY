#include "iostream"
using namespace std;
int main() {
	int n, x;
	cin >> n >> x;
	char* temp = new char[n];
	for (int i = 0; i < n; i++)
		cin >> temp[i];

	while (x) {
		for (int i = 0; i < n - 1; i++)
			if (temp[i] == 'B' && temp[i + 1] == 'G') {
				swap(temp[i], temp[i + 1]);
				i++;
			}
		x--;
	}
	for (int i = 0; i < n; i++)
		cout << temp[i];
}