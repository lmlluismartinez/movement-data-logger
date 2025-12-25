datalogger.onLogFull(function () {
    logging = false
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onButtonPressed(Button.A, function () {
    logging = true
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.AB, function () {
    logging = false
    basic.showIcon(IconNames.Skull)
    datalogger.deleteLog()
    datalogger.setColumnTitles(
    "x",
    "y",
    "z"
    )
})
input.onButtonPressed(Button.B, function () {
    logging = false
    basic.showIcon(IconNames.No)
})
let logging = false
logging = false
basic.showIcon(IconNames.Cow)
datalogger.setColumnTitles(
"x",
"y",
"z",
"Temperatura",
"Luz",
"Ruido",
"Brujula"
)
loops.everyInterval(15000, function () {
    if (logging) {
        datalogger.log(
        datalogger.createCV("x", input.acceleration(Dimension.X)),
        datalogger.createCV("y", input.acceleration(Dimension.Y)),
        datalogger.createCV("z", input.acceleration(Dimension.Z)),
        datalogger.createCV("Temperatura", input.temperature()),
        datalogger.createCV("Ruido", input.soundLevel()),
        datalogger.createCV("Brujula", input.compassHeading()),
        datalogger.createCV("Luz", input.lightLevel())
        )
    }
})
