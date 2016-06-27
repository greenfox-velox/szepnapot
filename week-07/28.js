'use strict';

var aa = [1, 2, 3];
var out = 0;
// if the aa list contains one element set the out to 1
// if the aa list contains two elements set the out to 2
// if the aa list contains more than 2 set the out to 10
// if the aa contains no elements set out to -1
if (0 < aa.length < 3) {
  out = aa.length;
} else if (aa.lenght > 2) {
  out = 10;
} else {
  out = -1;
}
