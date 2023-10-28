#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include "json.hpp"
#include "json_fwd.hpp"

using namespace std;
using nlohmann::json;
using nlohmann::ordered_json;

struct Fruit
{
    string name;
    int quantity;
    double price;
};

NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Fruit, name, quantity, price)

int main()
{
    json j1;
    j1["name"] = "Jack";
    j1["age"] = 21;
    j1["boy"] = true;
    j1["book"] = {"A", "B", "C"};

    cout << j1.dump() << endl;

    // json j2 = "{ \"flag\": true, \"price\": 3.45, \"name\": \"pencil\" }"_json;
    // cout << j2.dump() << endl;
    json j2 = R"({ "flag": true, "price": 3.45, "name": "pencil" })"_json;
    cout << j2.dump() << endl;

    Fruit fruit;
    fruit.name = "Apple";
    fruit.quantity = 10;
    fruit.price = 5.20;

    json j3 = fruit;
    cout << j3.dump() << endl;

    vector<int> vtTest{1, 2, 3, 4};
    json j4(vtTest);

    cout << j4.dump() << endl;

    std::map<std::string, int> mapTest{{"one", 1}, {"two", 2}, {"three", 3}};
    json j5(mapTest);
    cout << j5.dump() << endl;

    json j6;
    std::map<std::string, std::string> mapData{{"price", "11.23"}, {"name", "food"}};
    j6["data"] = mapData;
    j6["count"] = 1;
    cout << j6.dump() << endl;

    return 0;
}