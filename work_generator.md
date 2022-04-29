### Work Generator Experiment Tasks
Work generator should add a job type to all future jobs and future proof dockets documents and comments and the new job type called attachments

## Data/Redis
* Redis stores stuff in memory but it remembers it by rwriting to a dumb.rdb
* If restart redis if it finds dump then it reloads to memory
* If we can somehow write to a redis database redis writes a dump.rdb manually put it in ~data/redis next time system starts
* It will load those values into memory and achieve goal

# Program
* Write a program that will generate jobs and put it into a redis database
