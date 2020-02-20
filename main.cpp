#include <bits/stdc++.h>
#define endl '\n'

using namespace std;

int book_types, lib_cnt, days;
vector<int> book_score, signup_time, scans_per_day;
vector<vector<int>> books;

int eval(vector<pair<int, vector<int>>>& libs) {
    int score = 0;

    int n_libs = libs.size();
    vector<int> start_day(n_libs);
    for (int i = 0; i < n_libs; ++i) {
        start_day[i] = signup_time[libs[i].first];
    }
    partial_sum(start_day.begin(), start_day.end(), start_day.begin());

    vector<bool> scanned(book_types);

    for (int i = 0; i < n_libs; ++i) {
        cerr << "Library [" << libs[i].first << "]" << endl;
        int days_left = days - start_day[i];
        cerr << days_left << " days left" << endl;

        if (days_left < 0) {
            cerr << "Warning: days_left less than 0." << endl;
            continue;
        }

        int num_processed = min(days_left * scans_per_day[libs[i].first],
                                (int) libs[i].second.size());
        cerr << num_processed << " books will be processed" << endl;

        for (int j = 0; j < num_processed; ++j) {
            if (scanned[libs[i].second[j]]) continue;
            cerr << "Book " << libs[i].second[j] << " processed" << endl;
            scanned[libs[i].second[j]] = true;
            score += book_score[libs[i].second[j]];
        }
    }

    return score;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // Read input
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

    vector<pair<int, vector<int>>> libs = {{1, {5, 2, 3}},
                                           {0, {0, 1, 2, 3, 4}}};

    cout << eval(libs) << endl;

    return 0;
}
