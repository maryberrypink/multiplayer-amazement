def on_button_multiplayer_a_pressed(player2):
    global jump_count
    jump = 0
    jump_count += 1
    if jump > jump_count:
        mp.get_player_sprite(player2).x = -100
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def _2():
    tiles.set_current_tilemap(tilemap("""
        level6
    """))
    scene.center_camera_at(0, 0)
def _1():
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
        sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f 1 1 1 1 1 3 f . . . . 
                        . . . f 1 3 3 3 3 3 1 3 f . . . 
                        . . . f 3 3 f f f f 3 1 f . . . 
                        . . . f 3 f f d d f f 3 f . . . 
                        . . f 3 f d f d d f d f 3 f . . 
                        . . f 3 f d 3 d d 3 d f 3 f . . 
                        . . f 3 3 f d d d d f 3 3 f . . 
                        . f 3 3 f 3 f f f f 3 f 3 3 f . 
                        . . f f d 3 5 3 3 5 3 d f f . . 
                        . . f d d f 3 5 5 3 f d d f . . 
                        . . . f f f 3 3 3 3 f f f . . . 
                        . . . . . f 8 8 8 8 f . . . . . 
                        . . . . . f 8 f f 8 f . . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            SpriteKind.player))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
        sprites.create(img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            SpriteKind.player))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
        sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f 1 1 1 1 1 a f . . . . 
                        . . . f 1 a a a a a 1 a f . . . 
                        . . . f a a f f f f a 1 f . . . 
                        . . . f a f f d d f f a f . . . 
                        . . f a f d f d d f d f a f . . 
                        . . f a f d a d d a d f a f . . 
                        . . f a a f d d d d f a a f . . 
                        . f a a f a f f f f a f a a f . 
                        . . f f d a 5 a a 5 a d f f . . 
                        . . f d d f a 5 5 a f d d f . . 
                        . . . f f f a a a a f f f . . . 
                        . . . . . f c c c c f . . . . . 
                        . . . . . f c f f c f . . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).x = -100
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).x = -100
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).x = -100
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO))
jump_count = 0
_1()
_2()