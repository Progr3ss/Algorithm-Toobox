# Uses python3
import sys

def sort_values(weights, values):
  result = []
  for index, weight in enumerate(weights):
    result.append([index, values[index] / weight])

  return sorted(result, key=lambda x: x[1], reverse=True)


def get_optimal_value(capacity, weights, values):
  sorted_weight_indexes = sort_values(weights, values)

  capacity_left = capacity
  a = []
  best_value = 0
  for [index, coeff] in sorted_weight_indexes:
    if capacity_left == 0: return best_value

    volume_to_reduce = min(weights[index], capacity_left)
    capacity_left -= volume_to_reduce
    best_value += volume_to_reduce * coeff

  return best_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
