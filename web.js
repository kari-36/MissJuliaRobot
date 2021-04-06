//    MissJuliaRobot (A Telegram Bot Project)
//    Copyright (C) 2019-Present Anonymous (https://t.me/MissJulia_Robot)

//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU Affero General Public License as published by
//    the Free Software Foundation, in version 3 of the License.

//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU Affero General Public License for more details.

//    You should have received a copy of the GNU Affero General Public License
//    along with this program.  If not, see < https://www.gnu.org/licenses/agpl-3.0.en.html >


var express = require('express');

var app = express();

var newBaseURL = process.env.WEBSITE_URL || 'http://missjuliarobot.unaux.com';

var redirectStatus = parseInt(302);

var port = process.env.PORT || 5000;

app.get('*', function(request, response) {

  response.redirect(redirectStatus, newBaseURL + request.url);

});

app.listen(port, function() {

  console.log("\n" + "Listening on " + newBaseURL + " at port " + port + "\n");

});
