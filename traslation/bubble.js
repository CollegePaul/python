//convered version

var sorted_data, unsorted_data;

function bubble_sort(data) {
  var n;
  n = data.length;

  for (var i = 0, _pj_a = n - 1; i < _pj_a; i += 1) {
    for (var j = 0, _pj_b = n - i - 1; j < _pj_b; j += 1) {
      if (data[j] > data[j + 1]) {
        [data[j], data[j + 1]] = [data[j + 1], data[j]];
      }
    }
  }

  return data;
}

unsorted_data = [4, 2, 5, 3, 1, 7, 6];
sorted_data = bubble_sort(unsorted_data);
console.log(sorted_data);