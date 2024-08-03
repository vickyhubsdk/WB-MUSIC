let player;
let videoId = 'oBwrlePfchs'; // Replace with the YouTube video ID
let videoTitle = 'Alone Night -24 Mash-up l Lofi pupil | Bollywood spongs | Chillout Lo-fi Mix #KaranK2official'; // Replace with the YouTube video title

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player-container', {
    height: '0',
    width: '0',
    videoId: videoId,
    playerVars: {
      autoplay: 0,
      controls: 0,
      showinfo: 0,
      modestbranding: 1,
      loop: 1,
      playlist: videoId,
      key: 'YOUR_API_KEY' // Add your API key here
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}

function onPlayerReady(event) {
  event.target.playVideo();
  document.querySelector('.track-name').textContent = videoTitle;
}

function onPlayerStateChange(event) {
  if (event.data === YT.PlayerState.PLAYING) {
    document.querySelector('.playpause-track').innerHTML = '<i class="fa fa-pause-circle fa-5x"></i>';
  } else if (event.data === YT.PlayerState.PAUSED) {
    document.querySelector('.playpause-track').innerHTML = '<i class="fa fa-play-circle fa-5x"></i>';
  }
}

function playpauseTrack() {
  if (player.getPlayerState() === YT.PlayerState.PLAYING) {
    player.pauseVideo();
  } else {
    player.playVideo();
  }
}

function seekTo() {
  let seekSlider = document.querySelector('.seek_slider');
  let seekTime = seekSlider.value;
  player.seekTo(seekTime);
}

function setVolume() {
  let volumeSlider = document.querySelector('.volume_slider');
  let volume = volumeSlider.value;
  player.setVolume(volume);
}

function prevTrack() {
  console.log('Previous track');
}

function nextTrack() {
  console.log('Next track');
}
