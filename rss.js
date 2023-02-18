const RSS_URL = `https://codepen.io/picks/feed/`; //http://gizmodo.com/vip.xml

fetch(RSS_URL)
  .then(response => response.text())
  .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
  .then(data => console.log(data))
