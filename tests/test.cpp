#include <catch2/catch_test_macros.hpp>
#include "hello_world.hpp"

using namespace pydjinni::example;

TEST_CASE("Testing HelloWorld") {
    REQUIRE(HelloWorld::say_hello() == "hello from C++!");
}
