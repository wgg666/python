const JSEncrypt = require('node-jsencrypt');
function RSAencode(str, pubk) {
	var result = '';
	if (pubk && str) {
		var encrypt = new JSEncrypt();
		encrypt.setPublicKey(pubk);
		result = encrypt.encrypt(encodeURI(str));
	}
	return result;
}

function RSAencode(str, pubk) {
	var result = '';
	if (pubk && str) {
		// pubk = Base64.decode(pubk);
		// var encryptionExponent = '';
		// var modulus = '';
		// if(pubk){
		// 	encryptionExponent = pubk.split(',')[0];
		// 	modulus = pubk.split(',')[1];
		// }
		// if(encryptionExponent && modulus){
		// 	setMaxDigits(129);
		// 	var key = RSAUtils.getKeyPair(encryptionExponent, '', modulus);
		// 	result = RSAUtils.encryptedString(key, str);
		// }
		var encrypt = new JSEncrypt();
		encrypt.setPublicKey(pubk);
		result = encrypt.encrypt(encodeURI(str));
	}
	return result;
}

// function decrypt (msg) {
// 	let decrypt = new JSEncrypt()
// 	decrypt.setPrivateKey('MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC/M868kojjC5nTlW2VAXwWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh/Yqtv8eTpRQq6TCMyaU8u/vj5rZsqFR7wEOEL+zDdt7Xr/n7aoOwRDMYRPdnxV5PwyDLYrVGX4/x4+SxcpbflgchjPHx10ubEd7KM2QIDAQAB')
// 	var decryptMsg = decrypt.decrypt(msg)
// 	return decryptMsg
// }
// console.log(decrypt('a2iQYm8+LuE4z+nB0oJ6Vr6dgMTCwzz2J6HqPnh0ihWvj2Be0zSznS8dVb8E3irjzRwGaoVLIPgK9gRGlAwlxvJ9zOKIdkS/JioRH0peFiThmFqJqu4Vj+xqDWfpw40siqJ+EJuhIBWEQ/o/Pc0yzksMbUAd0WeQTEbm+H2xCW4='))
