using System;
using System.Text.Json;
using System.Text.Json.Serialization;

public class JsonDateTimeConverter : JsonConverter<DateTime>
{
	private readonly string _dateFormat;

	public JsonDateTimeConverter(string dateFormat)
	{
		_dateFormat = dateFormat;
	}

	public override DateTime Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
	{
		// Convert the short date string back to DateTime
		return DateTime.ParseExact(reader.GetString(), _dateFormat, null);
	}

	public override void Write(Utf8JsonWriter writer, DateTime value, JsonSerializerOptions options)
	{
		// Convert DateTime to the specified date string format
		writer.WriteStringValue(value.ToString(_dateFormat));
	}
}
