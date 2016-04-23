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
  for (var idx = 0, lengthh = (courses.length * 2); idx < lengthh; idx++) {
    html += '<tr><td class="col-lg-8"><div id="chart_' + idx + '"></div></td></tr>'
  }
  tableDiv.append(html);
}

function drawCircles(placeholder, courseName, index) {
  var h = 500;
  var w = 900;
  var minimumBubbleSize = 10;
  var labelsWithinBubbles = true;
  var title = "Relative Grades of Similar Students";
  var dataset = [{
    label: "Mercury",
    value: 1134,
    xPos: 0
  }, {
    label: "Venus ",
    value: 1134,
    xPos: 0
  }, {
    label: "Earth",
    value: 1134,
    xPos: 0
  }, {
    label: "Mars",
    value: 1134,
    xPos: 0
  }, {
    label: "Jupiter",
    value: 1134,
    xPos: 0
  }, {
    label: "Uranus",
    value: 1134,
    xPos: 0
  }, {
    label: "Neptune",
    value: 1134,
    xPos: 0
  }, {
    label: "Saturn",
    value: 1134,
    xPos: 0
  }];
  var gapBetweenBubbles = 15;
  var xPadding = 50;
  var yPadding = 100;
  var scaling = 20;

  /* Sort the dataset to ensure the bubble are always ascending */
  dataset = dataset.sort(function(a, b) {
    return (a.value - b.value);
  });

  /* Scale the dataset */
  var factor = minimumBubbleSize / dataset[0].value;
  dataset.forEach(function(d) {
    d.value = d.value * factor;
  });

  /* Scaling */

  function getRadius(area) {
    return Math.sqrt(area / Math.PI);
  }

  function getLabelDivSideFromArea(area) {
    return Math.sqrt(Math.pow(2 * rScale(area), 2) / 2);
  }

  var rScale = function(input) {
    /* Magic number here is just to get a reasonable sized smallest bubble */
    return getRadius(input) * scaling;
  }

  /* For bubbles that are too big to centre their text, compute a better position */

  function getNewXPosition(leftBubble, rightBubble) {

  }

  function getNewYPosition(leftBubble, rightBubble) {

  }

  /* Create the chart */

  var svg = d3.select("#" + placeholder)
    .append("svg")
    .attr("width", w)
    .attr("height", h)

  /* Adjust left hand side to add on the radius of the first bubble */
  xPaddingPlusRadius = xPadding + rScale(dataset[0].value);
  dataset[0].xPos = xPaddingPlusRadius;

  var circles = svg.selectAll("circle")
    .data(dataset)
    .enter()
    .append("circle");

  var accumulator = xPaddingPlusRadius;

  circles.attr("cx", function(d, i) {

      if (i > 0) {

        var previousRadius = rScale(dataset[i - 1].value);
        var currentRadius = rScale(d.value);

        var hypotenuseLength = previousRadius + currentRadius + gapBetweenBubbles;
        var yLength = currentRadius - previousRadius;

        var increment = Math.sqrt(Math.pow(hypotenuseLength, 2) - Math.pow(yLength, 2));
        accumulator += increment;
        d.xPos = accumulator;
        return accumulator;

      } else {
        return xPaddingPlusRadius;
      }

    })
    .attr("cy", function(d) {
      return h - rScale(d.value) - yPadding;
    })
    .attr("r", function(d) {
      return rScale(d.value);
    });

  /* Place text in the circles. Could try replacing this with foreignObject */

  svg.selectAll("foreignObject")
    .data(dataset)
    .enter()
    .append("foreignObject")
    .attr("x", function(d, i) {
      if (d.xPos > w) {
        /* Do the different thing */
        return d.xPos - (getLabelDivSideFromArea(d.value) / 2);
      } else {
        return d.xPos - (getLabelDivSideFromArea(d.value) / 2);
      }
    })
    .attr("y", function(d, i) {
      if (labelsWithinBubbles) {
        if ((h - rScale(d.value) - yPadding) < 0) {
          /* Do the different thing */
          return h - rScale(d.value) - yPadding - (getLabelDivSideFromArea(d.value) / 2);
        } else {
          return h - rScale(d.value) - yPadding - (getLabelDivSideFromArea(d.value) / 2);
        }
      } else {
        return h - yPadding + 20;
      }
    })
    .attr("width", function(d) {
      return getLabelDivSideFromArea(d.value);
    })
    .attr("height", function(d) {
      return getLabelDivSideFromArea(d.value);
    })
    .append("xhtml:body")
    .append("div")
    .attr("style", function(d) {
      return "width: " + getLabelDivSideFromArea(d.value) + "; height: " + getLabelDivSideFromArea(d.value);
    })
    .attr("class", "labelDiv")
    .html(function(d, i) {
      return "<p class='label'>" + d.label + "</p>";
    });

  /* Draw the chart title */

  svg.append("text")
    .text(title)
    .attr("x", xPadding)
    .attr("y", h - 40)
    .attr("class", "title");
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
  var data = google.visualization.arrayToDataTable(getData(placeholder.split("_")[1]));

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
  for (var idx = 0, lengthh = courses.length; idx < lengthh;) {
    var data = courses;
    (function(idx) {
      google.charts.setOnLoadCallback(function() {
        drawChart(data[idx].courseName, "chart_" + (idx));
      });
      drawCircles("chart_" + (idx + 1), data[idx].courseName, idx);
    })(idx);
    idx += 2;
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