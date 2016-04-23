var rowCounter = 0;

function addNewRow(rowId) {
    var html = '<tr class="dataRows" id="row_' + rowId + '">'
    html += '<td class="col-lg-2"><select class="form-control" id="courseID_' + rowId + '" name="courseID[' + (rowId) + ']">'
	html += '<option value="CSE1" selected="selected">CSE 1</option><option value="CSE2">CSE 2</option>'
    html += '<option value="CSE3">CSE 3</option><option value="CSE4">CSE 4</option>'
    html += '<option value="CSE5">CSE 5</option><option value="CSE6">CSE 6</option>'
    html += '<option value="CSE7">CSE 7</option><option value="CSE8">CSE 8</option>'
    html += '<option value="CSE9">CSE 9</option><option value="CSE10">CSE 10</option>'
    html += '<option value="CSE11">CSE 11</option><option value="CSE12">CSE 12</option>'
    html += '<option value="CSE13">CSE 13</option><option value="CSE14">CSE 14</option>'
    html += '<option value="CSE15">CSE 15</option><option value="CSE16">CSE 16</option>'
    html += '<option value="CSE17">CSE 17</option><option value="CSE18">CSE 18</option>'
    html += '<option value="CSE19">CSE 19</option><option value="CSE20">CSE 20</option>'
    html += '</select></td><td class="col-lg-2"><select class="form-control" id="expectedGrade_' + rowId + '" name="expectedGrade[' + (rowId)+ ']">'
    html += '<option value="A+" selected="selected">A+</option><option value="A">A</option>'
    html += '<option value="A-">A-</option><option value="B+">B+</option>'
    html += '<option value="B">B</option><option value="B-">B-</option>'
    html += '<option value="C+">C+</option><option value="C">C</option>'
    html += '<option value="C-">C-</option><option value="D">D</option>'
    html += '<option value="F">F</option></select></td>'
	html += '</tr>'
	$("#courseTable").append(html);
}

$("#addCourse").click(function() {
    rowCounter++;
	addNewRow(rowCounter);
});

$("#submitForm").click(function() {
    $("#hiddenRowCounter").val(rowCounter);
    console.log(rowCounter)
    $("#courseSelectionForm").submit();
})