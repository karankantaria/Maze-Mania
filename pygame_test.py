# ... [The rest of your imports and initializations]

coins_group = pygame.sprite.Group()
for y, row in enumerate(level_1):   # The coin will show up in the first level of the maze
    for x, cell in enumerate(row):
        if cell == "C":            # making coin == to c
            coin = Coin(x * TILE_SIZE, y * TILE_SIZE, COIN_IMAGE)  # The coin image will show and be placed in the maze 
            coins_group.add(coin)

# Main loop
loop=True
while loop:
    # ... [The rest of your loop code: movement, enemy collisions, etc.]

    # Check for collisions between the player and coins
    coin_collision = pygame.sprite.spritecollideany(player_init, coins_group)
    if coin_collision:
        coins_group.remove(coin_collision)  # Remove the coin from the group
        player_score += 1  # Increase score

    # Render the score
    score_text = font.render(f"score: {player_score}", True, (255,255,255)) 
    WINDOW.blit(score_text, (10,10))

    # Render coins
    draw_coins(coins_group)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.update()

# ... [Your other code]

pygame.quit()


    




