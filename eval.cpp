#include<bits/stdc++.h>
using namespace std;

int book_types, lib_cnt, days;
vector<int> book_score, signup_time, scans_per_day;
vector<vector<int>> books;
vector<pair<int, vector<int>>> libs;

int eval() {
    int score = 0;

    int n_libs = libs.size();
    vector<int> start_day(n_libs);
    for (int i = 0; i < n_libs; ++i) {
        start_day[i] = signup_time[libs[i].first];
    }
    partial_sum(start_day.begin(), start_day.end(), start_day.begin());

    vector<bool> scanned(book_types);

    for (int i = 0; i < n_libs; ++i) {
        int days_left = days - start_day[i];

        if (days_left < 0) {
            cerr << "Warning: days_left less than 0." << endl;
            continue;
        }

        int num_processed = min(days_left * scans_per_day[libs[i].first],
                                (int) libs[i].second.size());

        for (int j = 0; j < num_processed; ++j) {
            if (scanned[libs[i].second[j]]) continue;
            scanned[libs[i].second[j]] = true;
            score += book_score[libs[i].second[j]];
        }
    }

    return score;
}

void read_model() {
		cin >> book_types >> lib_cnt >> days;

    book_score.resize(book_types);
    signup_time.resize(lib_cnt);
    scans_per_day.resize(lib_cnt);
    books.resize(lib_cnt);

    for (int i = 0; i < book_types; ++i) {
        cin >> book_score[i];
    }

    for (int i = 0; i < lib_cnt; ++i) {
        int book_cnt;
        cin >> book_cnt >> signup_time[i] >> scans_per_day[i];
        for (int j = 0; j < book_cnt; ++j) {
            int id;
            cin >> id;
            books[i].push_back(id);
        }
    }
}

void read_target() {
	int n;
	cin >> n;
	while(n--) {
		int id;
		cin >> id;
		vector<int> bks;
		int m;
		cin >> m;
		while (m--) {
			int x;
			cin >> x;
			bks.push_back(x);
		}
		libs.push_back(make_pair(id, bks));
	}
}

int main(int argc, char *argv[]) {
  
	if(argc < 3) {
		cerr << "Required 2 files" << endl;		
  }

	freopen(argv[1],"r",stdin);
	read_model();
	freopen(argv[2], "r", stdin);
  read_target();
	cout << "Score is " << eval() << endl;		
}
