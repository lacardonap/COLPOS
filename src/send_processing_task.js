#!/usr/bin/env node

var amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var queue = 'processing_gps';
        var parameters = {'RINEX': '/home/grand/Desktop/TEST/bogt0590.20o',
                   'TYPE': 'PPP',
                   'EMAIL': 'leocardonapiedrahita@gmail.com'};

        channel.assertQueue(queue, {
            durable: false
        });
        channel.sendToQueue(queue, Buffer.from(JSON.stringify(parameters)));

        console.log(" [x] Sent %s", parameters);
    });
    setTimeout(function() {
        connection.close();
        process.exit(0);
    }, 500);
});