#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/pwm.h"

#define HAPTIC_PIN 16

uint slice_num;
int cps = 10000;

void setup_vibe() {
    gpio_set_function(HAPTIC_PIN, GPIO_FUNC_PWM);

    // Find out which slice is connected to the GPIO
    slice_num = pwm_gpio_to_slice_num(HAPTIC_PIN);


    // Enable the PWM slice
    pwm_set_enabled(slice_num, false);
}

void vibe(float duty) {

    // Set period (divider) and duty cycle
    pwm_set_enabled(slice_num, true);
    pwm_set_wrap(slice_num, cps); // 10000 counts per period
    pwm_set_chan_level(slice_num, PWM_CHAN_A, (uint16_t) cps*duty); // 50% duty cycle
}


int main() {
    stdio_init_all();
    setup_vibe();

    while (true) {
        vibe(0.5);
    }

}
