# alfareza

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT

initAlphaz() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing AlphaZ Plugins ..."
    assertEnvironment
    editLastMessage "Starting AlphaZ Plugins ..."
    printLine
}

startAlphaz() {
    startLogBotPolling
    runPythonModule alphaz "$@"
}

stopAlphaz() {
    sendMessage "Exiting AlphaZ Plugins ..."
    endLogBotPolling
    exit 0
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopAlphaz
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopAlphaz
    exit 130
}

runAlphaz() {
    initAlphaz
    startAlphaz "$@"
    stopAlphaz
}
