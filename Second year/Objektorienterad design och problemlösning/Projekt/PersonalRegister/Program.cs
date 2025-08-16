using PersonalRegister;
using System.Text.Json;

namespace PJU
{
	class Program
	{
		static async Task Main(string[] args)
		{
			var antRepository = new JsonPersonalRepository<Ant>("ants.json");
			var beeRepository = new JsonPersonalRepository<Bee>("bees.json");
			var personalService = new PersonalService(antRepository, beeRepository);

			// Load simulation state
			SimulationState simulationState = LoadSimulationState();
			DateTime currentDate = simulationState?.LastSimulatedDate ?? DateTime.Today;
			int startingWeek = simulationState?.WeekNumber ?? 1;

			// If simulation state is null, initialize ants and bees
			if (simulationState == null)
			{
				currentDate = DateTime.Today;
				startingWeek = 1;

				Console.WriteLine("Initializing ants and bees...");

				// Initialize 500,000 ants with random birthdates between 1 and 21 days ago
				var antFactory = new AntFactory();
				for (int i = 0; i < 500000; i++)
				{
					var randomAnt = antFactory.Create(currentDate);
					await antRepository.AddAsync(randomAnt);
				}

				// Save initial ants to file
				await antRepository.SaveToFileAsync();

				// Initialize 50,000 bees with similar random birthdates
				var beeFactory = new BeeFactory();
				for (int i = 0; i < 50000; i++)
				{
					var randomBee = beeFactory.Create(currentDate);
					await beeRepository.AddAsync(randomBee);
				}

				// Save initial bees to file
				await beeRepository.SaveToFileAsync();

				Console.WriteLine("Ants and bees initialized.");
			} 
			else
			{
				// If a previous state is found, load the last simulated date and start from the next week
				currentDate = simulationState.LastSimulatedDate;
				startingWeek = simulationState.WeekNumber + 1;

				Console.WriteLine($"Continuing simulation from Week {startingWeek - 1}: ");
			}

			// Simulate weekly operations
			for (int week = startingWeek; week < startingWeek + 4; week++)
			{
				Console.WriteLine($"\nWeek {week}:");
				await personalService.HandleWeeklyOperations(currentDate, week);
				currentDate = currentDate.AddDays(7); // Move time forward by one week for each iteration
			}

			Console.WriteLine("Simulation complete.");
		}

		// Load simulation state from JSON file
		static SimulationState LoadSimulationState()
		{
			string filePath = "simulation_state.json";
			if (System.IO.File.Exists(filePath))
			{
				string json = System.IO.File.ReadAllText(filePath);
				return JsonSerializer.Deserialize<SimulationState>(json);
			}
			return null;
		}
	}
}