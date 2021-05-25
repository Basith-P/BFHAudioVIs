function deleteAudio(audioId) {
   fetch("/delete-audio", {
      method: "POST",
      body: JSON.stringify({ audioId: audioId }),
   }).then((_res) => {
      window.location.href = "/";
   });
}

function runvis(audioId) {
   fetch("/rinvis", {
      method: "POST",
      body: JSON.stringify({ audioId: audioId }),
   }).then((_res) => {
      window.location.href = "/";
   });
}

// function runVis() {
//    $.ajax({
//       url: "vis.py",
//       context: document.body,
//    }).done(function () {
//       alert("awesome..!");
//    });
// }
