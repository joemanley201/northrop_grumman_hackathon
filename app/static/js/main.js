var rowCounter = 0;

function addNewRow(rowId) {
    var html = '<tr class="dataRows" id="row_' + rowId + '">'
    html += '<td class="col-lg-2"><select class="form-control" id="courseID_' + rowId + '" name="courseID[' + (rowId) + ']">'
	html += '<option value="CSE1" selected="selected">CSE 1</option><option value="CSE2" selected="selected">CSE 2</option>'
    html += '<option value="CSE3" selected="selected">CSE 3</option><option value="CSE4" selected="selected">CSE 4</option>'
    html += '<option value="CSE5" selected="selected">CSE 5</option><option value="CSE6" selected="selected">CSE 6</option>'
    html += '<option value="CSE7" selected="selected">CSE 7</option><option value="CSE8" selected="selected">CSE 8</option>'
    html += '<option value="CSE9" selected="selected">CSE 9</option><option value="CSE10" selected="selected">CSE 10</option>'
    html += '<option value="CSE11" selected="selected">CSE 11</option><option value="CSE12" selected="selected">CSE 12</option>'
    html += '<option value="CSE13" selected="selected">CSE 13</option><option value="CSE14" selected="selected">CSE 14</option>'
    html += '<option value="CSE15" selected="selected">CSE 15</option><option value="CSE16" selected="selected">CSE 16</option>'
    html += '<option value="CSE17" selected="selected">CSE 17</option><option value="CSE18" selected="selected">CSE 18</option>'
    html += '<option value="CSE19" selected="selected">CSE 19</option><option value="CSE20" selected="selected">CSE 20</option>'
    html += '</select></td><td class="col-lg-2"><select class="form-control" id="expectedGrade_' + rowId + '" name="expectedGrade[' + (rowId)+ ']">'
    html += '<option value="A+" selected="selected">A+</option><option value="A" selected="selected">A</option>'
    html += '<option value="A-" selected="selected">A-</option><option value="B+" selected="selected">B+</option>'
    html += '<option value="B" selected="selected">B</option><option value="B-" selected="selected">B-</option>'
    html += '<option value="C+" selected="selected">C+</option><option value="C" selected="selected">C</option>'
    html += '<option value="C-" selected="selected">C-</option><option value="D" selected="selected">D</option>'
    html += '<option value="F" selected="selected">F</option></select></td>'
	html += '</tr>'
	$("#courseTable").append(html);
	rowCounter++;
}

$("#addCourse").click(function() {
	addNewRow(rowCounter);
});

$("#submitForm").click(function() {
    $("#hiddenRowCounter").val(rowCounter);
    console.log(rowCounter)
    $("#courseSelectionForm").submit();
})