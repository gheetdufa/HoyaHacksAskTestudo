document.addEventListener('DOMContentLoaded', function () {
  const chatHistory = document.getElementById('chat-history');
  const userInputField = document.getElementById('user-input-field');
  const sendButton = document.getElementById('send-button');
  const animatedFace = document.getElementById('animated-face');

  function appendMessage(message, sender) {
      const messageElement = document.createElement('div');
      messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';
      messageElement.textContent = message;
      chatHistory.appendChild(messageElement);
  }

  function sendMessage() {
      const message = userInputField.value.trim();
      if (message !== '') {
          appendMessage(message, 'user');
          // Add logic here to generate bot response
          // For now, let's simulate a response after a short delay
          setTimeout(() => {
              const response = "I'm your chatbot!";
              appendMessage(response, 'bot');
              // Simulate the animated face talking
              animateFace();
          }, 500);
          userInputField.value = '';
      }
  }

  function animateFace() {
      // Add your animation logic here, e.g., changing CSS classes or styles
      animatedFace.classList.add('talking');
      // Use ResponsiveVoice for speech synthesis
      responsiveVoice.speak('Hello, I am your chatbot!', 'UK English Female');
      // Reset the animation after a delay
      setTimeout(() => {
          animatedFace.classList.remove('talking');
      }, 2000); // Adjust the delay as needed
  }

  sendButton.addEventListener('click', sendMessage);

  userInputField.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {
          sendMessage();
      }
  });
});
// script.js
var audio = document.getElementById("audio");
var audioButton = document.getElementById("audioButton");

audioButton.addEventListener("click", toggleAudio);

function toggleAudio() {
    if (audio.paused) {
        audio.play().catch(function(error) {
            console.error('Error playing audio:', error);
        });
        audioButton.textContent = "Pause Audio";
    } else {
        audio.pause();
        audioButton.textContent = "Play Audio";
    }
}




