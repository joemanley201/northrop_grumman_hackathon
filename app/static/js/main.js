var rowCounter = 2;

function addNewRow(rowId) {
    var html = '<tr class="dataRows" id="row_' + rowId + '">'
    html += '<td class="col-lg-2"><select class="form-control" id="courseID_' + rowId + '">" name="courseID">'
	html += '<option value="CSE 1" selected="selected">CSE 1</option><option value="CSE 2" selected="selected">CSE 2</option>'
    html += '<option value="CSE 3" selected="selected">CSE 3</option><option value="CSE 4" selected="selected">CSE 4</option>'
    html += '<option value="CSE 5" selected="selected">CSE 5</option><option value="CSE 6" selected="selected">CSE 6</option>'
    html += '<option value="CSE 7" selected="selected">CSE 7</option><option value="CSE 8" selected="selected">CSE 8</option>'
    html += '<option value="CSE 9" selected="selected">CSE 9</option><option value="CSE 10" selected="selected">CSE 10</option>'
    html += '<option value="CSE 11" selected="selected">CSE 11</option><option value="CSE 12" selected="selected">CSE 12</option>'
    html += '<option value="CSE 13" selected="selected">CSE 13</option><option value="CSE 14" selected="selected">CSE 14</option>'
    html += '<option value="CSE 15" selected="selected">CSE 15</option><option value="CSE 16" selected="selected">CSE 16</option>'
    html += '<option value="CSE 17" selected="selected">CSE 17</option><option value="CSE 18" selected="selected">CSE 18</option>'
    html += '<option value="CSE 19" selected="selected">CSE 19</option><option value="CSE 20" selected="selected">CSE 20</option>'
    html += '</select></td><td class="col-lg-2"><select class="form-control" id="expectedGrade_' + rowId + '">" name="expectedGrade">'
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
    $("#courseSelectionForm").submit();
})