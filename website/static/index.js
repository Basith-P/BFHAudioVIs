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
>>>>>>> 2c78b0b24b602f53646f4294c60118152a2260f7
