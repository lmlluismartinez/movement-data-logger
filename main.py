def on_log_full():
    global logging
    logging = False
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
datalogger.on_log_full(on_log_full)

def on_button_pressed_a():
    global logging
    logging = True
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global logging
    logging = False
    basic.show_icon(IconNames.SKULL)
    datalogger.delete_log()
    datalogger.set_column_titles("x", "y", "z")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global logging
    logging = False
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

logging = False
logging = False
basic.show_icon(IconNames.NO)
datalogger.set_column_titles("x", "y", "z", "Temperatura", "Luz", "Ruido", "Brujula")

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("x", input.acceleration(Dimension.X)),
            datalogger.create_cv("y", input.acceleration(Dimension.Y)),
            datalogger.create_cv("z", input.acceleration(Dimension.Z)),
            datalogger.create_cv("Temperatura", input.temperature()),
            datalogger.create_cv("Ruido", input.sound_level()),
            datalogger.create_cv("Brujula", input.compass_heading()),
            datalogger.create_cv("Luz", input.light_level()))
loops.every_interval(100, on_every_interval)
