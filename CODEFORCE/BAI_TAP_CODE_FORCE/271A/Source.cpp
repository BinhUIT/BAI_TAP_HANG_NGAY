#include "iostream"
#include "set"
using namespace std;

bool checkDistinctYear(int n) {
	set<char> temp;
	while (n != 0) {
		temp.insert(n % 10);
		n /= 10;
	}
	if (temp.size() == 4)
		return 1;
	return 0;
}

int main() {
	int n;
	cin >> n;
	int i = n + 1;
	while (!checkDistinctYear(i))
		i++;
	cout << i;
}