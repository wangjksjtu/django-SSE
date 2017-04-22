### Environment ###

* Python2.7
* Python-packages urllib2/urllib/httplib/json/base64

###

### Useages ##

    h = Http_ClientServer("http://wangjksjtu.com.cn:2117/")
    h.getAll() // get all ciphertexts
    h.add('1111001001', "0b2952b0d93576dd24b49dcb66a9c7d8") // add one ciphertext
    h.update(17, '1111001001', "0b2952b0d93576dd24b49dcb66dfc7d8") // update one ciphertext (17 is id)	  
    h.search('1111001001') // search ciphertexts with keystring
    h.delete(17) // delete one ciphertext
    
You can check in http://www.wangjksjtu.com.cn:2117/ where you should sign in first.
* Username: test
* Password: testpassword
