import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

public class MainTest {

    @Test
    public void testBasicScenario() {
        List<Integer> passengerLocations = List.of(1, 5, 10);
        List<Integer> taxiLocations = List.of(2, 6, 12);
        List<Integer> demand = List.of(1, 2, 1);
        List<Integer> trafficConditions = List.of(0, 1, 2);

        List<Integer> result = Main.taxiDispatch(passengerLocations, taxiLocations, demand, trafficConditions);

        // Check that the result is not empty
        assertFalse(result.isEmpty());
        // Check that the result has the correct size
        assertEquals(passengerLocations.size(), result.size());
    }

    @Test
    public void testNoPassengers() {
        List<Integer> passengerLocations = List.of();
        List<Integer> taxiLocations = List.of(2, 6, 12);
        List<Integer> demand = List.of(1, 2, 1);
        List<Integer> trafficConditions = List.of(0, 1, 2);

        List<Integer> result = Main.taxiDispatch(passengerLocations, taxiLocations, demand, trafficConditions);

        // Check that the result is empty since there are no passengers
        assertTrue(result.isEmpty());
    }

    @Test
    public void testNoTaxis() {
        List<Integer> passengerLocations = List.of(1, 5, 10);
        List<Integer> taxiLocations = List.of();
        List<Integer> demand = List.of(1, 2, 1);
        List<Integer> trafficConditions = List.of(0, 1, 2);

        List<Integer> result = Main.taxiDispatch(passengerLocations, taxiLocations, demand, trafficConditions);

        // Check that the result is empty since there are no taxis
        assertTrue(result.isEmpty());
    }

    @Test
    public void testEqualPassengersAndTaxis() {
        List<Integer> passengerLocations = List.of(1, 5, 10);
        List<Integer> taxiLocations = List.of(2, 6, 12);
        List<Integer> demand = List.of(1, 1, 1);
        List<Integer> trafficConditions = List.of(0, 1, 2);

        List<Integer> result = Main.taxiDispatch(passengerLocations, taxiLocations, demand, trafficConditions);

        // Check that the result is not empty
        assertFalse(result.isEmpty());
        // Check that the result has the correct size
        assertEquals(passengerLocations.size(), result.size());
    }

    @Test
    public void testEmptyInput() {
        List<Integer> passengerLocations = List.of();
        List<Integer> taxiLocations = List.of();
        List<Integer> demand = List.of();
        List<Integer> trafficConditions = List.of();

        List<Integer> result = Main.taxiDispatch(passengerLocations, taxiLocations, demand, trafficConditions);

        // Check that the result is empty since there are no passengers or taxis
        assertTrue(result.isEmpty());
    }
}
```