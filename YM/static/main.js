let player;

let videoId = 'oBwrlePfchs'; // Replace with the YouTube video ID

let videoTitle = 'Alone Night -24 Mash-up l Lofi pupil | Bollywood spongs | Chillout Lo-fi Mix #KaranK2official'; // Replace with the YouTube video title



// Initialize the YouTube player

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

      key: 'AIzaSyBz5NX4HAyvsz4o8FvjTe9t8irKL5gNVY8' // Add your API key here

    },

    events: {

      'onReady': onPlayerReady,

      'onStateChange': onPlayerStateChange

    }

  });

}



// Set up the player when it's ready

function onPlayerReady(event) {

  event.target.playVideo();

  document.querySelector('.track-name').textContent = videoTitle;

}



// Update the player state when it changes

function onPlayerStateChange(event) {

  if (event.data === YT.PlayerState.PLAYING) {

    document.querySelector('.playpause-track').innerHTML = '<i class="fa fa-pause-circle fa-5x"></i>';

  } else if (event.data === YT.PlayerState.PAUSED) {

    document.querySelector('.playpause-track').innerHTML = '<i class="fa fa-play-circle fa-5x"></i>';

  }

}



// Play/pause the track

function playpauseTrack() {

  if (player.getPlayerState() === YT.PlayerState.PLAYING) {

    player.pauseVideo();

  } else {

    player.playVideo();

  }

}



// Seek to a specific time in the track

function seekTo() {

  let seekSlider = document.querySelector('.seek_slider');

  let seekTime = seekSlider.value;

  player.seekTo(seekTime);

}



// Set the volume of the track

function setVolume() {

  let volumeSlider = document.querySelector('.volume_slider');

  let volume = volumeSlider.value;

  player.setVolume(volume);

}



// Previous track (not implemented)

function prevTrack() {

  console.log('Previous track');

}



// Next track (not implemented)

function nextTrack() {

  console.log('Next track');

}
