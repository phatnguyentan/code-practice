import { ChainEvents } from "./ChainEvents";
import { GetConversationEvent } from "./events/GetConversationEvent";
import { SelectConversation } from "./events/SelectConversation";
import { GetMessageEvent } from "./events/GetMessageEvent";

let chainEvents = new ChainEvents();
chainEvents.addEvents(
  new GetConversationEvent(chainEvents),
  new SelectConversation(chainEvents),
  new GetMessageEvent(chainEvents)
);
chainEvents.start();
