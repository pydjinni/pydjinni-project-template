#include "hello_world.hpp"

using namespace pydjinni::example;

std::string HelloWorld::say_hello() {
    return "hello from C++!";
}

void HelloWorld::call_me(const std::function<void(std::string)> & callback) {
    callback("callback from C++");
}
