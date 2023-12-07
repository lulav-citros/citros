
# added by `citros setup-ssh`
if [ -z "$SSH_AUTH_SOCK" ]; then
    # Check if the file exists and attempt to use it
    if [ -f $HOME/.ssh/ssh-agent ]; then
        eval `cat $HOME/.ssh/ssh-agent`
    fi

    # After attempting to use the file, check if the agent is still running
    if [ -n "$SSH_AGENT_PID" ] && kill -0 $SSH_AGENT_PID 2>/dev/null; then
        # Agent is running, so nothing more to do
        :
    else
        # If the file doesn't exist, or the agent isn't running, start a new agent
        ssh-agent -s &> $HOME/.ssh/ssh-agent
        eval `cat $HOME/.ssh/ssh-agent`
    fi
fi
