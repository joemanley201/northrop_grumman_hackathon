var courses = [];

function zipper(metrics, currentScores, targetScores) {
  var response = [];
  response.push(["Metric", "Current", "Target"])
  for (var idx = 0, lengthh = metrics.length; idx < lengthh; idx++) {
    response.push([metrics[idx], currentScores[idx], targetScores[idx]])
  }
  return response;
}

function populateTable() {
  var tableDiv = $("#analysisTable");
  html = ""
  for (var idx = 0, lengthh = courses.length; idx < lengthh; idx++) {
    html += '<tr><td class="col-lg-8"><div id="chart_' + idx + '"></div></td></tr>'
  }
  tableDiv.append(html);
}

function populateResponse(response) {
  for (var i = 0, course_length = response.course_list.length; i < course_length; i++) {
    var currData = {};
    currData.closestGrades = response.closest_grades_list[i];
    currData.currentScores = response.current_student_list[i];
    currData.targetScores = response.original_list[i];
    currData.metrics = response.metric_list[i];
    currData.courseName = response.course_list[i];
    courses.push(currData);
  }
  console.log(courses);

}

function getData(idx) {
  var course = courses[idx];
  var data = zipper(course.metrics, course.currentScores, course.targetScores);
  return data;
}

function drawChart(courseName, placeholder) {
  var data = google.visualization.arrayToDataTable(getData(0));

  var options = {
    width: 900,
    height: 500,
    chart: {
      title: 'Comparison for Course ' + courseName
    },
    hAxis: {
      title: ''
    },
    vAxis: {
      title: 'Metrics',
      minValue: 0,
      maxValue: 100
    },
    bars: 'horizontal'
  };
  var material = new google.charts.Bar(document.getElementById(placeholder));
  material.draw(data, options);
}

$(document).ready(function() {
  populateResponse(response);
  populateTable();
  google.charts.load('current', {
    packages: ['corechart', 'bar']
  });
  for (var idx = 0, lengthh = courses.length; idx < lengthh; idx++) {
    var data = courses;
    (function(idx) {
      google.charts.setOnLoadCallback(function() {
        drawChart(data[idx].courseName, "chart_" + (idx));
      });
    })(idx);
  }


  $('#test1').bind('click', function() {
    $.ajax({
      url: '/testAjax',
      type: 'POST',
      data: [1, 2, 3, 4, 5],
      contentType: 'application/json;charset=UTF-8',
      success: function(evt) {
        alert(evt.data);
      }
    });
    return false;
  });

});