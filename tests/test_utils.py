from testbench_sardine import utils


def test_pizza_size_standard_behavior():
    result = utils.pizza_size(5)
    assert result > 19.63 and result < 19.64


def test_pizza_size_special_behavior():
    result = utils.pizza_size(666)
    assert result == 666
