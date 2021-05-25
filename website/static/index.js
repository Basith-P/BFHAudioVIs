function deleteAudio(audioId) {
   fetch("/delete-audio", {
      method: "POST",
      body: JSON.stringify({ audioId: audioId }),
   }).then((_res) => {
      window.location.href = "/";
   });
}
