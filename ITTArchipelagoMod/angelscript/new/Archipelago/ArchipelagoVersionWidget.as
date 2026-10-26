// Archipelago: mod version in the bottom left.
const FString ARCHIPELAGO_MOD_VERSION = "0.1.2";

class UArchipelagoVersionWidget : UHazeUserWidget
{
	UFont Font;

	UFUNCTION(BlueprintOverride)
	void Construct()
	{
		SetVisibility(ESlateVisibility::HitTestInvisible);
		// Default engine font.
		Font = Cast<UFont>(LoadObject(nullptr, "/Engine/EngineFonts/Roboto.Roboto"));
	}

	UFUNCTION(BlueprintOverride)
	void OnPaint(FPaintContext& Context) const
	{
		FGeometry Geometry = GetCachedGeometry();
		FText Text = FText::FromString("AP " + ARCHIPELAGO_MOD_VERSION);
		// Grey text with a faint shadow.
		FVector2D Position = FVector2D(10.f, Geometry.LocalSize.Y - 19.f);
		WidgetBlueprint::DrawTextFormatted(Context, Text, Position + FVector2D(1.f, 1.f), Font, 12, n"Light", FLinearColor(0.f, 0.f, 0.f, 0.35f));
		WidgetBlueprint::DrawTextFormatted(Context, Text, Position, Font, 12, n"Light", FLinearColor(0.7f, 0.7f, 0.7f, 0.7f));
	}
}
