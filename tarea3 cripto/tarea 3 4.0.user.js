// ==UserScript==
// @name         tarea (final)
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  3DES - OFB
// @author       You
// @match        file:///C:/Users/RV/Downloads/archivo_tarea.html
// @require      https://raw.githubusercontent.com/brix/crypto-js/develop/src/core.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// @require      https://raw.githubusercontent.com/brix/crypto-js/develop/src/cipher-core.js
// @require      https://raw.githubusercontent.com/brix/crypto-js/develop/src/enc-base64.js
// @require      https://raw.githubusercontent.com/brix/crypto-js/develop/src/tripledes.js
// @require      https://raw.githubusercontent.com/brix/crypto-js/develop/src/mode-ofb.js
// @require      https://raw.githubusercontent.com/brix/crypto-js/develop/src/pad-nopadding.js
// updateURL
// @update
// @grant        none
// ==/UserScript==

(function() {
    // enc: base64 -> wordarray
    var base64_cipher = document.getElementsByClassName("tripledes")[0].getAttribute("id");
    var cipher_text = CryptoJS.enc.Base64.parse(base64_cipher);
    // key: utf8->wordarray
    var key = document.getElementsByClassName("key")[0].getAttribute("id");
    key = CryptoJS.enc.Utf8.parse(key);
    // se crea la iv, extrayendola del texto cifrado
    var iv = cipher_text.clone();
    iv.sigBytes = 8; // bytes para la IV
    iv.clamp();
    cipher_text.words.splice(0, 2); // se elimina la IV del texto cifrado
    cipher_text.sigBytes -= 8; // se eliminan los bytes correspondientes a la IV
    // desencriptacion
    var decrypted = CryptoJS.TripleDES.decrypt({ciphertext: cipher_text}, key, {
      iv: iv,
      mode: CryptoJS.mode.OFB,
      padding: CryptoJS.pad.NoPadding
    });
    var msg = document.getElementsByClassName("mensaje")[0];
    msg.innerText = decrypted.toString(CryptoJS.enc.Utf8);
})();