# jazz

Chatbot to send notifications to slack.

Currently enabled funcionts:

- /bazooka "mensagem" @mention to @mention - its purpose is to allow you to send "bazookas" anonymously to slack's "bazooka-nutella" channel.

![jazz](https://github.com/madeiramadeirabr/jazz/blob/production/jazz/jazz.jpg)
> Nice little place to enjoy, huh?

# Requirements
- Python 3.7 ou superior

# Working local with docker

change *environment:* variables in *docker-compose.yaml*

after that run this command:

```bash
$ docker-compose up
```

The API Doc can be accessed at: http://localhost:5000/docs

#Todo

- limpar branches merged dos projetos no git;
- acionamento do CLI de criação de agctions nos repositórios do git;
- busca de documentos no jira
- ...