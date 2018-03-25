const Light = require('./Light');
const LightOnCommand = require('./LightOnCommand');
const SimpleRemoteControl = require('./SimpleRemoteControl');

// receiver
const light = new Light();
// concrete command
const lightOnCommand = new LightOnCommand(light);
// invoker
const simpleRemoteCotroll = new SimpleRemoteControl();
simpleRemoteCotroll.setCommand(lightOnCommand);
simpleRemoteCotroll.pressButton();
