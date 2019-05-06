function mongooseConnect(){
	var mongoose = require('mongoose');
	var url = "mongodb+srv://webReadOnly:readOnly@tpa-whplr.mongodb.net/test?retryWrites=true";

	mongoose.connect(url, function(err) {
		if (err) throw err;
		console.log('Conectado')
	});

}

mongooseConnect();