mp.onButtonEvent(mp.MultiplayerButton.A, ControllerButtonEvent.Pressed, function (player2) {
    let jump = 0
    jump_count += 1
    if (jump > jump_count) {
        mp.getPlayerSprite(player2).x = -100
    }
})
function _2 () {
    tiles.setCurrentTilemap(tilemap`level6`)
    scene.centerCameraAt(0, 60)
}
function _1 () {
    mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), sprites.create(img`
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
        `, SpriteKind.Player))
    mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), sprites.create(img`
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
        `, SpriteKind.Player))
    mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three), sprites.create(img`
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
        `, SpriteKind.Player))
    mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).x = -100
    mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)).x = -100
    mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three)).x = -100
    mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Two))
}
let jump_count = 0
_1()
_2()
