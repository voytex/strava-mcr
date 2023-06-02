// document.addEventListener("DOMContentLoaded", function () {
//   document
//     .getElementById("csvFileInput")
//     .addEventListener("change", function (e) {
//       var file = e.target.files[0];
//       if (file) {
//         Papa.parse(file, {
//           header: true,
//           complete: function (results) {
//             var jsonData = results.data;
//             console.log(jsonData);
//             // Do further processing with the JSON data
//             // ...
//           },
//         });
//       }
//     });
// });

// ===============================================
// variables
// ===============================================
var allActivities,
  bikeActivities,
  otherActivities,
  totalBikeKm,
  totalOtherKm,
  bikeLeaderboard,
  otherLeaderboard;

// ===============================================
// File import
// ===============================================
const fileInput = document.getElementById("csvFileInput");
fileInput.addEventListener("change", (e) => {
  var file = e.target.files[0];
  console.log(file);
  if (!file) {
    alert("Invalid or missing file!");
    return;
  }
  Papa.parse(file, {
    header: true,
    transformHeader: (field) => {
      // Wird bug with "Type" key...
      if (field.trim() === '"Type"') return "Typ";
      else return field;
    },
    dynamicTyping: true,
    complete: (results) => {
      console.log(results);
      allActivities = results.data;
    },
  });
});

// ===============================================
// Processing
// ===============================================
function filterActivitiesByMonth(activities, month) {
  if (month === 0) return activities;
  return activities.filter(
    (activity) => new Date(activity["Date"]).getMonth() == month
  );
}

function filterActivitesByType(activities, type) {
  return activities.filter((activity) => activity["Typ"] == type);
}

function filterActivitesByTypeNegated(activites, type) {
  return activites.filter((activity) => activity["Typ"] != type);
}

function getTotalKm(activites) {
  var sum = 0.0;
  activites.forEach((activity) => {
    sum += activity.Distance;
  });
  return sum.toFixed(2);
}

function createLeaderboard(activities) {
  var athletes = [];
  activities.forEach((activity) => {
    var athlete = athletes.find((a) => a.name === activity.Name);
    if (athlete) {
      athlete.distance += activity.Distance;
    } else {
      var newAthlete = {
        name: activity.Name,
        distance: activity.Distance,
      };
      athletes.push(newAthlete);
    }
  });
  return athletes.sort((a1, a2) => a2.distance - a1.distance);
}

const month = document.getElementById("monthInput");
const button = document.getElementById("btnShow");
const totalBikeDistanceElement = document.getElementById("totalBikeDistance");
const totalOtherDistanceElement = document.getElementById("totalOtherDistance");
const bikeLeaderboardElement = document.getElementById("bikeLeaderboard");
const otherLeaderboardElement = document.getElementById("otherLeaderboard");

button.onclick = function () {
  var monthToShow = new Date(month.value);
  monthToShow = monthToShow.getMonth();
  console.log(allActivities);
  var allActivitiesByMonth = filterActivitiesByMonth(
    allActivities,
    monthToShow
  );
  bikeActivities = filterActivitesByType(allActivitiesByMonth, "Ride");
  otherActivities = filterActivitesByTypeNegated(allActivitiesByMonth, "Ride");
  console.log(allActivitiesByMonth);
  console.log(bikeActivities);
  console.log(otherActivities);
  console.log(getTotalKm(bikeActivities));
  console.log(getTotalKm(otherActivities));
  console.log(getTotalKm(allActivities));
  bikeLeaderboard = createLeaderboard(bikeActivities);
  otherLeaderboard = createLeaderboard(otherActivities);
  console.log(bikeLeaderboard);
  console.log(otherLeaderboard);

  totalBikeDistanceElement.innerHTML = getTotalKm(bikeActivities) + " km";
  totalOtherDistanceElement.innerHTML = getTotalKm(otherActivities) + " km";

  document.querySelectorAll("h4").forEach((item) => (item.hidden = false));
  document.querySelectorAll("h3").forEach((item) => (item.hidden = false));
  bikeLeaderboardElement.innerHTML = "";

  bikeLeaderboard.forEach((athlete) => {
    bikeLeaderboardElement.innerHTML +=
      "<tr><td>" +
      athlete.name +
      "</td><td>" +
      athlete.distance.toFixed(2) +
      " km</td></tr>";
  });
  otherLeaderboardElement.innerHTML = "";
  otherLeaderboard.forEach((athlete) => {
    otherLeaderboardElement.innerHTML +=
      "<tr><td>" +
      athlete.name +
      "</td><td>" +
      athlete.distance.toFixed(2) +
      " km</td></tr>";
  });
};
